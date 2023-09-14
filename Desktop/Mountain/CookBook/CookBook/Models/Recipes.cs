using System.ComponentModel.DataAnnotations;

namespace CookBook.Models
{
    public class Recipe
    {
        [Key] public long IdR { get; set; }
        public string? NameR { get; set; }
        public string? Image { get; set; }
        public int Time { get; set; }
        public int NumPers { get; set; }
        public string? Type { get; set; }
        public string? Ingredients { get; set; }
        public string? Instructions { get; set; }

    }
        /*public class Tags
        {
            public long IdT { get; set; }
            public string NameT { get; set; }
            public string TypeT { get; set; }

        }
        public class TagsRecipe
        {
            public long IdT { get; set; }
            public long IdR { get; set; }

        }*/
}
