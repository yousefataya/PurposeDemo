using System.ComponentModel.DataAnnotations;

namespace PurposeCMS.Users.Dto
{
    public class ChangeUserLanguageDto
    {
        [Required]
        public string LanguageName { get; set; }
    }
}