using RimWorld;
using Verse;
using Harmony;
using System.Reflection;

namespace {{cookiecutter.package_name}}
{
	//This is your main class and its constructor. Because it inherits RimWorlds' Mod class, will get called by RimWorld when it starts up.
    public class {{cookiecutter.package_name}} : Mod
    {
        public static HarmonyInstance harmony = HarmonyInstance.Create("{{cookiecutter.author.replace(' ', '_')}}.RimWorld.{{cookiecutter.package_name}}");

        public {{cookiecutter.package_name}}(ModContentPack content) : base(content)
        {
            
            
            harmony.PatchAll(Assembly.GetExecutingAssembly());
        }
    }
}