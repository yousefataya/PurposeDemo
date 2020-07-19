using System.Data.Common;
using Microsoft.EntityFrameworkCore;

namespace PurposeCMS.EntityFrameworkCore
{
    public static class PurposeCMSDbContextConfigurer
    {
        public static void Configure(DbContextOptionsBuilder<PurposeCMSDbContext> builder, string connectionString)
        {
            builder.UseSqlServer(connectionString);
        }

        public static void Configure(DbContextOptionsBuilder<PurposeCMSDbContext> builder, DbConnection connection)
        {
            builder.UseSqlServer(connection);
        }
    }
}
