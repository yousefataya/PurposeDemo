using System.Threading.Tasks;
using Abp.Authorization;
using Abp.Runtime.Session;
using PurposeCMS.Configuration.Dto;

namespace PurposeCMS.Configuration
{
    [AbpAuthorize]
    public class ConfigurationAppService : PurposeCMSAppServiceBase, IConfigurationAppService
    {
        public async Task ChangeUiTheme(ChangeUiThemeInput input)
        {
            await SettingManager.ChangeSettingForUserAsync(AbpSession.ToUserIdentifier(), AppSettingNames.UiTheme, input.Theme);
        }
    }
}
