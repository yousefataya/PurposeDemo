using Abp.AutoMapper;
using Abp.Modules;
using Abp.Reflection.Extensions;
using PurposeCMS.Authorization;

namespace PurposeCMS
{
    [DependsOn(
        typeof(PurposeCMSCoreModule), 
        typeof(AbpAutoMapperModule))]
    public class PurposeCMSApplicationModule : AbpModule
    {
        public override void PreInitialize()
        {
            Configuration.Authorization.Providers.Add<PurposeCMSAuthorizationProvider>();
        }

        public override void Initialize()
        {
            var thisAssembly = typeof(PurposeCMSApplicationModule).GetAssembly();

            IocManager.RegisterAssemblyByConvention(thisAssembly);

            Configuration.Modules.AbpAutoMapper().Configurators.Add(
                // Scan the assembly for classes which inherit from AutoMapper.Profile
                cfg => cfg.AddMaps(thisAssembly)
            );
        }
    }
}
