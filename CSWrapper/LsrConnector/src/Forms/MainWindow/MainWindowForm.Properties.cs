using System.ComponentModel;

namespace LsrConnector.Forms.MainWindow;

partial class MainWindowForm
{
    public Button SelectResultDirectoryButton
    {
        get => selectResultDirectoryButton;
        set => selectResultDirectoryButton = value;
    }

    public TextBox ResultDirectoryTextBox
    {
        get => resultDirectoryTextBox;
        set => resultDirectoryTextBox = value;
    }

    public IContainer Components
    {
        get => components;
        set => components = value;
    }

    public Panel MainPanel
    {
        get => mainPanel;
        set => mainPanel = value;
    }

    public Button StartButton
    {
        get => startButton;
        set => startButton = value;
    }

    public GroupBox OutputGroupBox
    {
        get => outputGroupBox;
        set => outputGroupBox = value;
    }

    public TextBox OutputTextBox
    {
        get => outputTextBox;
        set => outputTextBox = value;
    }

    public GroupBox ScriptParametersGroupBox
    {
        get => scriptParametersGroupBox;
        set => scriptParametersGroupBox = value;
    }

    public Button SelectSecondFileButton
    {
        get => selectSecondFileButton;
        set => selectSecondFileButton = value;
    }

    public Label SecondFilePathLabel
    {
        get => secondFilePathLabel;
        set => secondFilePathLabel = value;
    }

    public TextBox SecondFilePathTextBox
    {
        get => secondFilePathTextBox;
        set => secondFilePathTextBox = value;
    }

    public Button SelectFirstFileButton
    {
        get => selectFirstFileButton;
        set => selectFirstFileButton = value;
    }

    public Label FirstFilePathLabel
    {
        get => firstFilePathLabel;
        set => firstFilePathLabel = value;
    }

    public TextBox FirstFilePathTextBox
    {
        get => firstFilePathTextBox;
        set => firstFilePathTextBox = value;
    }

    public Button SelectPythonButton
    {
        get => selectPythonButton;
        set => selectPythonButton = value;
    }

    public Label PythoonPathLabel
    {
        get => pythonPathLabel;
        set => pythonPathLabel = value;
    }

    public TextBox PythonPathTextBox
    {
        get => pythonPathTextBox;
        set => pythonPathTextBox = value;
    }
}