using System.Threading.Tasks;
using Abp.Application.Services;
using Abp.Application.Services.Dto;
using PurposeCMS.Roles.Dto;
using PurposeCMS.Users.Dto;

namespace PurposeCMS.Users
{
    public interface IUserAppService : IAsyncCrudAppService<UserDto, long, PagedUserResultRequestDto, CreateUserDto, UserDto>
    {
        Task<ListResultDto<RoleDto>> GetRoles();

        Task ChangeLanguage(ChangeUserLanguageDto input);
    }
}
