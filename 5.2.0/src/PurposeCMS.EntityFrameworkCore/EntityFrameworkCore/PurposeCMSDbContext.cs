using Microsoft.EntityFrameworkCore;
using Abp.Zero.EntityFrameworkCore;
using PurposeCMS.Authorization.Roles;
using PurposeCMS.Authorization.Users;
using PurposeCMS.MultiTenancy;

namespace PurposeCMS.EntityFrameworkCore
{
    public class PurposeCMSDbContext : AbpZeroDbContext<Tenant, Role, User, PurposeCMSDbContext>
    {
        /* Define a DbSet for each entity of the application */
        
        public PurposeCMSDbContext(DbContextOptions<PurposeCMSDbContext> options)
            : base(options)
        {
        }
    }
}
