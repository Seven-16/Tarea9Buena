using System.ComponentModel.DataAnnotations;

public class Tardanza
{
    public string Titulo { get; set; }
    public string Descripcion { get; set; }
    public string ImagenUrl { get; set; }
    public DateTime Fecha {get; set;} = DateTime.Now;
}