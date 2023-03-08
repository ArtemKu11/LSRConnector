using LsrConnector.Forms.MainWindow;

namespace LsrConnector.Utils.OutputTextBoxChangeProcessor;

public class OutputTextBoxProcessor
{
    private readonly object _locker = new();
    private readonly TextBox _outputTextBox;
    private readonly MainWindowForm _mainWindowForm;
    private string _lastPrintedMessage = "";
    private string LastPrintedMessage
    {
        get
        {
            lock (_locker)
            {
                return _lastPrintedMessage;
            }
        }
    }

    public OutputTextBoxProcessor(TextBox outputTextBox, MainWindowForm mainWindowForm)
    {
        _outputTextBox = outputTextBox;
        _mainWindowForm = mainWindowForm;
    }

    public void PrintLineWithTime(string line, bool checkDuplicate = false)
    {
        PrintLine(DateTime.Now.ToLongTimeString() + " " + line, checkDuplicate);
    }
    
    public void PrintLine(string line, bool checkDuplicate = false)
    {
        if (!(checkDuplicate && !DuplicateCheck(line)))
        {
            PrintIntoTextBox(line);
        }
        
    }

    private void PrintIntoTextBox(string line)
    {
        lock (_locker)
        {
            if (_mainWindowForm is { IsDisposed: false })
            {
                if (_mainWindowForm.InvokeRequired)
                {
                    _mainWindowForm.Invoke(() =>
                    {
                        _outputTextBox.AppendText(line + "\r\n");
                        _lastPrintedMessage = line;
                    });
                }
                else
                {
                    _outputTextBox.AppendText(line + "\r\n");
                    _lastPrintedMessage = line;
                }
            }
        }
    }

    private bool DuplicateCheck(string line)
    {
        return !line.Equals(LastPrintedMessage);
    }
}