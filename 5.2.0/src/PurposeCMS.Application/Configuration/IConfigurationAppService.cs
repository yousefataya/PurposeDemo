using System.Threading.Tasks;
using PurposeCMS.Configuration.Dto;

namespace PurposeCMS.Configuration
{
    public interface IConfigurationAppService
    {
        Task ChangeUiTheme(ChangeUiThemeInput input);
    }
}
