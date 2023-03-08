using System.Diagnostics;
using LsrConnector.Forms.MainWindow;
using LsrConnector.Service.DTO;
using LsrConnector.Utils.CmdProcessCreator;
using LsrConnector.Utils.OutputTextBoxChangeProcessor;
using LsrConnector.Utils.PythonPathUtils;

namespace LsrConnector.Service.MainWindow;

public class MainWindowFormService
{
    private readonly MainWindowForm _mainWindowForm;
    private Process? _pythonConnectProcess;
    private readonly OutputTextBoxProcessor _outputTextBoxProcessor;
    private volatile bool _processRunFlag;

    public MainWindowFormService(MainWindowForm mainWindowForm)
    {
        _mainWindowForm = mainWindowForm;
        _outputTextBoxProcessor = new OutputTextBoxProcessor(_mainWindowForm.OutputTextBox, _mainWindowForm);
        InitializePythonPath();
    }

    private void InitializePythonPath()
    {
        var pythonPathHolder = new PythonPathLoader().ReadPythonPathFromDisk();
        if (pythonPathHolder == null)
        {
            MessageBox.Show("Питон путь установлен по умолчанию: cmd команда \"python\"");
            _mainWindowForm.PythonPathTextBox.Text = "python";
        }
        else
        {
            _mainWindowForm.PythonPathTextBox.Text = pythonPathHolder.PythonPath;
        }
    }

    private void ReadPythonPathOnDisk()
    {
        var pythonPath = _mainWindowForm.PythonPathTextBox.Text;
        if (pythonPath is "") return;
        var pythonPathHolder = new PythonPathHolder();
        pythonPathHolder.PythonPath = pythonPath;
        new PythonPathLoader().WritePythonPathOnDisk(pythonPathHolder);
    }
    
    public void SelectPython()
    {
        var openFileDialog = ResolveOpenFileDialog(new FilterFormatHolder(FilterFormatEnum.Exe));
        if (openFileDialog.ShowDialog() != DialogResult.Cancel)
        {
            var filePath = openFileDialog.FileName;
            if (filePath != null)
            {
                _mainWindowForm.PythonPathTextBox.Text = filePath;
                return;
            }

            MessageBox.Show(caption: @"Фатальная ошибка", text: @"Не удалось выбрать файл");
        }
    }
    
    private OpenFileDialog ResolveOpenFileDialog(FilterFormatHolder filterFormatHolder)
    {
        
        var openFileDialog = new OpenFileDialog();
        openFileDialog.Filter = filterFormatHolder.ToString();
        openFileDialog.FilterIndex = 1;
        return openFileDialog;
    }

    public void SelectFirstFile()
    {
        var openFileDialog = ResolveOpenFileDialog(new FilterFormatHolder(FilterFormatEnum.Lsr));
        if (openFileDialog.ShowDialog() != DialogResult.Cancel)
        {
            var filePath = openFileDialog.FileName;
            if (filePath != null)
            {
                _mainWindowForm.FirstFilePathTextBox.Text = filePath;
                ResolveResultDirectory(filePath);
                return;
            }

            MessageBox.Show(caption: @"Фатальная ошибка", text: @"Не удалось выбрать файл");
        }
    }

    private void ResolveResultDirectory(string filePath)
    {
        var lastIndexOfSlash = filePath.LastIndexOf("\\", StringComparison.Ordinal);
        if (_mainWindowForm.ResultDirectoryTextBox.Text is "")
        {
            _mainWindowForm.ResultDirectoryTextBox.Text = filePath[..lastIndexOfSlash];
        }
    }
    
    public void SelectSecondFile()
    {
        var openFileDialog = ResolveOpenFileDialog(new FilterFormatHolder(FilterFormatEnum.Lsr));
        if (openFileDialog.ShowDialog() != DialogResult.Cancel)
        {
            var filePath = openFileDialog.FileName;
            if (filePath != null)
            {
                _mainWindowForm.SecondFilePathTextBox.Text = filePath;
                return;
            }

            MessageBox.Show(caption: @"Фатальная ошибка", text: @"Не удалось выбрать файл");
        }
    }
    
    public void ExecuteCloseEvents()
    {
        ReadPythonPathOnDisk();
    }

    public void SelectResultFolder()
    {
        var selectedDirectory = ShowFolderBrowserDialog();
        if (selectedDirectory == null) return;
        _mainWindowForm.ResultDirectoryTextBox.Text = selectedDirectory;
    }
    
    private string? ShowFolderBrowserDialog()
    {
        
        var folderBrowserDialog = new FolderBrowserDialog();
        folderBrowserDialog.ShowNewFolderButton = false;
        if (folderBrowserDialog.ShowDialog() == DialogResult.OK)
        {
            return folderBrowserDialog.SelectedPath;
        }

        return null;
    }

    public void StartPythonScript()
    {
        if (!_processRunFlag)
        {
            RunScript();
        }
        else
        {
            KillScript();
        }
        
    }

    private void RunScript()
    {
        if (ValidateValues())
        {
            var pythonPath = _mainWindowForm.PythonPathTextBox.Text;
            var firstFilePath = _mainWindowForm.FirstFilePathTextBox.Text;
            var secondFilePath = _mainWindowForm.SecondFilePathTextBox.Text;
            var resultFilePath = ResolveResultFilePath();
            _pythonConnectProcess = new ProcessCreator().CreatePythonConnectProcess(pythonPath, firstFilePath, secondFilePath, resultFilePath);
            var processTask = new Task(AsyncStart);
            processTask.Start();
        }   
    }

    private void KillScript()
    {
        if (_pythonConnectProcess != null && !_pythonConnectProcess.HasExited)
        {
            _pythonConnectProcess.Kill();
            _outputTextBoxProcessor.PrintLine("Процесс убит");
        }
        else
        {
            _outputTextBoxProcessor.PrintLine("Процесс уже закончился");
        }

        _processRunFlag = false;
        _mainWindowForm.StartButton.Text = "Запустить";
    }

    private void AsyncStart()
    {
        if (_pythonConnectProcess != null)
        {
            _mainWindowForm.Invoke(() =>
            { 
                _mainWindowForm.OutputTextBox.Text = "";
                _mainWindowForm.StartButton.Text = "Убить процесс";
            });
            _processRunFlag = true;

            _pythonConnectProcess.OutputDataReceived += DataReceivedEventHandler;
            _pythonConnectProcess.ErrorDataReceived += DataReceivedEventHandler;
            
            _pythonConnectProcess.Start();
            _pythonConnectProcess.BeginOutputReadLine();
            _pythonConnectProcess.BeginErrorReadLine();
            _outputTextBoxProcessor.PrintLine("Скрипт запущен\r\n");
            _pythonConnectProcess.WaitForExit();
            
            _processRunFlag = false;

            _mainWindowForm.Invoke(() =>
            { 
                _mainWindowForm.StartButton.Text = "Запустить";
            });
        }
    }

    private void DataReceivedEventHandler(object sender, DataReceivedEventArgs e)
    {
        if (e.Data != null) _outputTextBoxProcessor.PrintLine(e.Data);
    }

    private string ResolveResultFilePath()
    {
        var resultFilePath = _mainWindowForm.ResultDirectoryTextBox.Text + "\\result.lsr";
        var counter = 1;
        while (File.Exists(resultFilePath)) 
        {
            resultFilePath = _mainWindowForm.ResultDirectoryTextBox.Text + $"\\result_{counter}.lsr";
            ++counter;
        }

        return resultFilePath;
    }

    private bool ValidateValues()
    {
        var pythonPath = _mainWindowForm.PythonPathTextBox.Text;
        var firstFilePath = _mainWindowForm.FirstFilePathTextBox.Text;
        var secondFilePath = _mainWindowForm.SecondFilePathTextBox.Text;
        var resultDirectoryPath = _mainWindowForm.ResultDirectoryTextBox.Text;

        var errorText = "";
        if (!pythonPath.Equals("python")) CheckValue("\"Python path\"", pythonPath, ref errorText);
        CheckValue("\"Путь до первого файла\"", firstFilePath, ref errorText);
        CheckValue("\"Путь до второго файла\"", secondFilePath, ref errorText);
        
        if (resultDirectoryPath is "" or null)
        {
            errorText += $"Неверное значение поля \"Путь до директории с результатом\"\n\n";
        }
        else
        {
            if (!Directory.Exists(resultDirectoryPath))
            {
                errorText += $"{resultDirectoryPath} не существует\n\n";
            }
        }

        if (!errorText.Equals(""))
        {
            MessageBox.Show(errorText);
            return false;
        }

        return true;
    }

    private void CheckValue(string valueName, string valuePath, ref string errorText)
    {
        if (valuePath is "" or null)
        {
            errorText += $"Неверное значение поля {valueName}\n\n";
        }
        else
        {
            if (!File.Exists(valuePath))
            {
                errorText += $"{valuePath} не существует\n\n";
            }
        }
    }

    public void ResolveNewSize(Control control)
    {
        var newHeight = control.Height;
        ResolveNewHeight(newHeight);
        var newWidth = control.Width;
        ResolveNewWidth(newWidth);
    }

    private void ResolveNewHeight(int newHeight)
    {
        var mainPanelHeight = newHeight - 59;
        _mainWindowForm.MainPanel.Height = mainPanelHeight;
        var outputGroupHeight = mainPanelHeight - 55 - _mainWindowForm.OutputGroupBox.Location.Y;
        _mainWindowForm.OutputGroupBox.Height = outputGroupHeight;
        var outputTextBoxHeight = outputGroupHeight - 14 - _mainWindowForm.OutputTextBox.Location.Y;
        _mainWindowForm.OutputTextBox.Height = outputTextBoxHeight;
        _mainWindowForm.StartButton.Location = new Point(_mainWindowForm.StartButton.Location.X, 
            (_mainWindowForm.OutputGroupBox.Location.Y + outputGroupHeight + 19));
    }

    private void ResolveNewWidth(int newWidth)
    {
        var mainPanelWidth = newWidth - 40;
        _mainWindowForm.MainPanel.Width = mainPanelWidth;
        var groupBoxesWidth = mainPanelWidth - 162 * 2;
        _mainWindowForm.ScriptParametersGroupBox.Width = groupBoxesWidth;
        _mainWindowForm.OutputGroupBox.Width = groupBoxesWidth;
        _mainWindowForm.OutputTextBox.Width = groupBoxesWidth - 96 * 2;
        var pathTextBoxesWidth = groupBoxesWidth - 454;
        _mainWindowForm.PythonPathTextBox.Width = pathTextBoxesWidth;
        _mainWindowForm.FirstFilePathTextBox.Width = pathTextBoxesWidth;
        _mainWindowForm.SecondFilePathTextBox.Width = pathTextBoxesWidth;
        _mainWindowForm.ResultDirectoryTextBox.Width = pathTextBoxesWidth;
        var buttonsX = _mainWindowForm.PythonPathTextBox.Location.X + pathTextBoxesWidth + 25;
        _mainWindowForm.SelectPythonButton.Location =
            new Point(buttonsX, _mainWindowForm.SelectPythonButton.Location.Y);
        _mainWindowForm.SelectFirstFileButton.Location =
            new Point(buttonsX, _mainWindowForm.SelectFirstFileButton.Location.Y);
        _mainWindowForm.SelectSecondFileButton.Location =
            new Point(buttonsX, _mainWindowForm.SelectSecondFileButton.Location.Y);
        _mainWindowForm.SelectResultDirectoryButton.Location =
            new Point(buttonsX, _mainWindowForm.SelectResultDirectoryButton.Location.Y);
        _mainWindowForm.StartButton.Location = new Point(mainPanelWidth / 2 - _mainWindowForm.StartButton.Width / 2,
            _mainWindowForm.StartButton.Location.Y);
    }
}