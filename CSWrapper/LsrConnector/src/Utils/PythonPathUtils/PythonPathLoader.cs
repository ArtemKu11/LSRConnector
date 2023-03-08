using System.Text.Json;

namespace LsrConnector.Utils.PythonPathUtils;

public class PythonPathLoader
{
    public void WritePythonPathOnDisk(PythonPathHolder pythonPathHolder)
    {
        ResolveDirectory();
        using FileStream fs = new FileStream("JSON\\python_path.json", FileMode.Create);
        JsonSerializer.Serialize(fs, pythonPathHolder);
    }

    private void ResolveDirectory()
    {
        if (!Directory.Exists("JSON"))
        {
            Directory.CreateDirectory("JSON");
        }
    }

    public PythonPathHolder? ReadPythonPathFromDisk()
    {
        if (File.Exists("JSON\\python_path.json"))
        {
            using (FileStream fs = new FileStream("JSON\\python_path.json", FileMode.OpenOrCreate))
            {
                try
                {
                    var pythonPathHolder = JsonSerializer.Deserialize(fs, typeof(PythonPathHolder));
                    if (pythonPathHolder != null)
                    {
                        return (PythonPathHolder)pythonPathHolder;
                    }
                    MessageBox.Show("Фатальная ошибка.\nПитон путь десериализовался в null");
                }
                catch (Exception)
                {
                    MessageBox.Show("Фатальная ошибка.\nПитон путь не десериализовался вообще");
                }
                
            }
        }
        else
        {
            MessageBox.Show("Файла с Питон путем не обнаружилось");
        }

        return null;
    }
}