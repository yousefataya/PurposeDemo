using Abp.Application.Services;
using PurposeCMS.MultiTenancy.Dto;

namespace PurposeCMS.MultiTenancy
{
    public interface ITenantAppService : IAsyncCrudAppService<TenantDto, int, PagedTenantResultRequestDto, CreateTenantDto, TenantDto>
    {
    }
}

