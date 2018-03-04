using RimWorld;
using Verse;

namespace {{cookiecutter.package_name}}
{
	//This is your main class and its constructor. Because it inherits the mod class, will get called by RimWorld when it starts up.
    public class {{cookiecutter.package_name}} : Mod
    {
    	public {{cookiecutter.package_name}}(ModContentPack content) : base(content)
        {
            
        }
    }
}