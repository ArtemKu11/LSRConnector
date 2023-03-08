using System.Diagnostics;

namespace LsrConnector.Utils.CmdProcessCreator;

public class ProcessCreator
{
    public Process CreatePythonConnectProcess(string pythonPath, string firstFilePath, string secondFilePath, string resultFilePath)
    {
        var connectProcess = new Process();
        var processStartInfo = new ProcessStartInfo();
        var cmdString = $"-u PythonModules\\LsrConnector\\src\\cmd_main.py {firstFilePath} {secondFilePath} {resultFilePath}";
        processStartInfo.FileName = pythonPath;
        processStartInfo.Arguments = cmdString;
        processStartInfo.RedirectStandardOutput = true;
        processStartInfo.RedirectStandardError = true;
        processStartInfo.UseShellExecute = false;
        processStartInfo.CreateNoWindow = true;
        connectProcess.StartInfo = processStartInfo;
        return connectProcess;
    }
}