using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Design;
using Microsoft.Extensions.Configuration;
using PurposeCMS.Configuration;
using PurposeCMS.Web;

namespace PurposeCMS.EntityFrameworkCore
{
    /* This class is needed to run "dotnet ef ..." commands from command line on development. Not used anywhere else */
    public class PurposeCMSDbContextFactory : IDesignTimeDbContextFactory<PurposeCMSDbContext>
    {
        public PurposeCMSDbContext CreateDbContext(string[] args)
        {
            var builder = new DbContextOptionsBuilder<PurposeCMSDbContext>();
            var configuration = AppConfigurations.Get(WebContentDirectoryFinder.CalculateContentRootFolder());

            PurposeCMSDbContextConfigurer.Configure(builder, configuration.GetConnectionString(PurposeCMSConsts.ConnectionStringName));

            return new PurposeCMSDbContext(builder.Options);
        }
    }
}
