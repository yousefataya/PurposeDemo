using Abp.Authorization;
using PurposeCMS.Authorization.Roles;
using PurposeCMS.Authorization.Users;

namespace PurposeCMS.Authorization
{
    public class PermissionChecker : PermissionChecker<Role, User>
    {
        public PermissionChecker(UserManager userManager)
            : base(userManager)
        {
        }
    }
}
