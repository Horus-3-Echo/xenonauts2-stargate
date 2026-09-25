using System;
using System.Collections.Generic;
using Artitas;
using Common.Content;
using Common.Modding;
using HarmonyLib;
using UnityEngine;

namespace StargateX2
{
    public sealed class StargateModLifecycle : IModLifecycle
    {
        public void Create(Mod mod, Harmony patcher)
        {
            Debug.Log("[XSG] loaded version=0.1.0");
        }

        public void Destroy()
        {
            Debug.Log("[XSG] unloaded");
        }

        public void OnWorldCreate(IModLifecycle.Section section, WeakReference<World> world)
        {
            Debug.Log("[XSG] world-created section=" + section);
        }

        public void OnWorldDispose(IModLifecycle.Section section, WeakReference<World> world)
        {
            Debug.Log("[XSG] world-disposed section=" + section);
        }

        public IEnumerable<Descriptor> GetRequiredAssets(IModLifecycle.Section section)
        {
            return Array.Empty<Descriptor>();
        }
    }
}
