using System.Threading.Tasks;
using Abp.Application.Services;
using PurposeCMS.Sessions.Dto;

namespace PurposeCMS.Sessions
{
    public interface ISessionAppService : IApplicationService
    {
        Task<GetCurrentLoginInformationsOutput> GetCurrentLoginInformations();
    }
}
