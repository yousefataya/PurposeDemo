using System.Threading.Tasks;
using Abp.Application.Services;
using PurposeCMS.Authorization.Accounts.Dto;

namespace PurposeCMS.Authorization.Accounts
{
    public interface IAccountAppService : IApplicationService
    {
        Task<IsTenantAvailableOutput> IsTenantAvailable(IsTenantAvailableInput input);

        Task<RegisterOutput> Register(RegisterInput input);
    }
}
