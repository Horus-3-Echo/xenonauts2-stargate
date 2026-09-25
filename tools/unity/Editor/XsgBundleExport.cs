#if UNITY_EDITOR
using System;
using System.IO;
using System.Linq;
using UnityEditor;
using UnityEngine;

namespace StargateX2.Authoring
{
    // Editor-only candidate. See docs/XSG-011A-ASSET-EXPORT.md for required evidence.
    // The caller supplies the verified X2 asset name; this helper cannot derive it.
    public static class XsgBundleExport
    {
        public static AssetBundleManifest Build(
            string prefabAssetPath,
            string verifiedAssetName,
            string bundleName,
            string emptyOutputDirectory,
            string expectedUnityVersion,
            BuildTarget targetPlatform)
        {
            RequireValue(prefabAssetPath, nameof(prefabAssetPath));
            RequireValue(verifiedAssetName, nameof(verifiedAssetName));
            RequireValue(bundleName, nameof(bundleName));
            RequireValue(emptyOutputDirectory, nameof(emptyOutputDirectory));
            RequireValue(expectedUnityVersion, nameof(expectedUnityVersion));

            if (!string.Equals(Application.unityVersion, expectedUnityVersion, StringComparison.Ordinal))
                throw new InvalidOperationException("Use the verified Unity Editor version before export.");

            if (!prefabAssetPath.StartsWith("Assets/", StringComparison.Ordinal)
                || !prefabAssetPath.EndsWith(".prefab", StringComparison.Ordinal)
                || prefabAssetPath.Contains("\\")
                || prefabAssetPath.Split('/').Any(part => part == ".." || part == "." || part == ""))
                throw new ArgumentException("Select a saved prefab under this Unity project's Assets/.", nameof(prefabAssetPath));

            if (AssetDatabase.LoadAssetAtPath<GameObject>(prefabAssetPath) == null)
                throw new ArgumentException("The prefab must exist and be imported before export.", nameof(prefabAssetPath));

            // This filename policy belongs to our exporter, not a claim about X2 naming rules.
            if (!bundleName.EndsWith(".assetbundle", StringComparison.Ordinal)
                || bundleName.Length <= ".assetbundle".Length
                || bundleName.Any(c => !(c >= 'a' && c <= 'z')
                    && !(c >= '0' && c <= '9') && c != '_' && c != '-' && c != '.'))
                throw new ArgumentException("Use one lowercase .assetbundle filename with no directory segments.", nameof(bundleName));

            if (!Directory.Exists(emptyOutputDirectory)
                || Directory.EnumerateFileSystemEntries(emptyOutputDirectory).Any())
                throw new ArgumentException("Select an existing empty staging directory.", nameof(emptyOutputDirectory));

            // Unity also writes a manifest bundle named after the output directory.
            if (string.Equals(new DirectoryInfo(emptyOutputDirectory).Name, bundleName, StringComparison.OrdinalIgnoreCase))
                throw new ArgumentException("The staging directory name must differ from the bundle name.", nameof(emptyOutputDirectory));

            var builds = new[]
            {
                new AssetBundleBuild
                {
                    assetBundleName = bundleName,
                    assetNames = new[] { prefabAssetPath },
                    // Unity's built-in load name override, not an Addressables package dependency.
                    addressableNames = new[] { verifiedAssetName }
                }
            };

            var manifest = BuildPipeline.BuildAssetBundles(
                emptyOutputDirectory, builds, BuildAssetBundleOptions.None, targetPlatform);
            if (manifest == null)
                throw new InvalidOperationException("AssetBundle build failed; retain the Unity Editor log.");

            Debug.Log("[XSG-EXPORT] unity-version=" + Application.unityVersion
                + " target=" + targetPlatform + " bundle=" + bundleName
                + " asset-name=" + verifiedAssetName);
            return manifest;
        }

        private static void RequireValue(string value, string parameter)
        {
            if (string.IsNullOrWhiteSpace(value))
                throw new ArgumentException("A verified non-empty value is required.", parameter);
        }
    }
}
#endif
