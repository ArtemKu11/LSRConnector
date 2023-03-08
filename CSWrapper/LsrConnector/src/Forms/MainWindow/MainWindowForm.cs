using LsrConnector.Service.MainWindow;

namespace LsrConnector.Forms.MainWindow
{
    public partial class MainWindowForm : Form
    {
        private readonly MainWindowFormService _mainWindowFormService;
        public MainWindowForm()
        {
            InitializeComponent();
            _mainWindowFormService = new MainWindowFormService(this);
        }

        private void SelectPythonButton_Click(object sender, EventArgs e)
        {
            _mainWindowFormService.SelectPython();
        }

        private void SelectFirstFileButton_Click(object sender, EventArgs e)
        {
            _mainWindowFormService.SelectFirstFile();
        }

        private void SelectSecondFileButton_Click(object sender, EventArgs e)
        {
            _mainWindowFormService.SelectSecondFile();
        }

        private void SelectResultDirectoryButton_Click(object sender, EventArgs e)
        {
            _mainWindowFormService.SelectResultFolder();
        }
        
        private void StartButton_Click(object sender, EventArgs e)
        {
            _mainWindowFormService.StartPythonScript();
        }

        private void MainForm_FormClosing(object sender, FormClosingEventArgs e)
        {
            _mainWindowFormService.ExecuteCloseEvents();
        }
        

        private void MainPanel_Click(object sender, EventArgs e)
        {
            ActiveControl = startButton;
        }

        private void OutputGroupBox_MouseCaptureChanged(object sender, EventArgs e)
        {
            ActiveControl = startButton;
        }

        private void ScriptParametersGroupBox_MouseCaptureChanged(object sender, EventArgs e)
        {
            ActiveControl = startButton;
        }

        private void MainWindowForm_SizeChanged(object sender, EventArgs e)
        {
            _mainWindowFormService.ResolveNewSize((Control) sender);
        }
    }
}