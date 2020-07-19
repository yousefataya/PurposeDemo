using Abp.AspNetCore.Mvc.Controllers;
using Abp.IdentityFramework;
using Microsoft.AspNetCore.Identity;

namespace PurposeCMS.Controllers
{
    public abstract class PurposeCMSControllerBase: AbpController
    {
        protected PurposeCMSControllerBase()
        {
            LocalizationSourceName = PurposeCMSConsts.LocalizationSourceName;
        }

        protected void CheckErrors(IdentityResult identityResult)
        {
            identityResult.CheckErrors(LocalizationManager);
        }
    }
}
