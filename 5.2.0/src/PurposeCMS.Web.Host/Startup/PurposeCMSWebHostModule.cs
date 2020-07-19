using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Configuration;
using Abp.Modules;
using Abp.Reflection.Extensions;
using PurposeCMS.Configuration;

namespace PurposeCMS.Web.Host.Startup
{
    [DependsOn(
       typeof(PurposeCMSWebCoreModule))]
    public class PurposeCMSWebHostModule: AbpModule
    {
        private readonly IWebHostEnvironment _env;
        private readonly IConfigurationRoot _appConfiguration;

        public PurposeCMSWebHostModule(IWebHostEnvironment env)
        {
            _env = env;
            _appConfiguration = env.GetAppConfiguration();
        }

        public override void Initialize()
        {
            IocManager.RegisterAssemblyByConvention(typeof(PurposeCMSWebHostModule).GetAssembly());
        }
    }
}
