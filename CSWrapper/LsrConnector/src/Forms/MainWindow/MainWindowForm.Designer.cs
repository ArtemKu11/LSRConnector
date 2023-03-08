namespace LsrConnector.Forms.MainWindow
{
    partial class MainWindowForm
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MainWindowForm));
            this.mainPanel = new System.Windows.Forms.Panel();
            this.startButton = new System.Windows.Forms.Button();
            this.outputGroupBox = new System.Windows.Forms.GroupBox();
            this.outputTextBox = new System.Windows.Forms.TextBox();
            this.scriptParametersGroupBox = new System.Windows.Forms.GroupBox();
            this.selectResultDirectoryButton = new System.Windows.Forms.Button();
            this.selectSecondFileButton = new System.Windows.Forms.Button();
            this.secondFilePathLabel = new System.Windows.Forms.Label();
            this.resultDirectoryLabel = new System.Windows.Forms.Label();
            this.secondFilePathTextBox = new System.Windows.Forms.TextBox();
            this.selectFirstFileButton = new System.Windows.Forms.Button();
            this.resultDirectoryTextBox = new System.Windows.Forms.TextBox();
            this.firstFilePathLabel = new System.Windows.Forms.Label();
            this.firstFilePathTextBox = new System.Windows.Forms.TextBox();
            this.selectPythonButton = new System.Windows.Forms.Button();
            this.pythonPathLabel = new System.Windows.Forms.Label();
            this.pythonPathTextBox = new System.Windows.Forms.TextBox();
            this.mainPanel.SuspendLayout();
            this.outputGroupBox.SuspendLayout();
            this.scriptParametersGroupBox.SuspendLayout();
            this.SuspendLayout();
            // 
            // mainPanel
            // 
            this.mainPanel.Controls.Add(this.startButton);
            this.mainPanel.Controls.Add(this.outputGroupBox);
            this.mainPanel.Controls.Add(this.scriptParametersGroupBox);
            this.mainPanel.Location = new System.Drawing.Point(12, 12);
            this.mainPanel.Name = "mainPanel";
            this.mainPanel.Size = new System.Drawing.Size(1154, 604);
            this.mainPanel.TabIndex = 0;
            this.mainPanel.Click += new System.EventHandler(this.MainPanel_Click);
            // 
            // startButton
            // 
            this.startButton.Location = new System.Drawing.Point(516, 568);
            this.startButton.Name = "startButton";
            this.startButton.Size = new System.Drawing.Size(112, 23);
            this.startButton.TabIndex = 10;
            this.startButton.Text = "Запустить";
            this.startButton.UseVisualStyleBackColor = true;
            this.startButton.Click += new System.EventHandler(this.StartButton_Click);
            // 
            // outputGroupBox
            // 
            this.outputGroupBox.Controls.Add(this.outputTextBox);
            this.outputGroupBox.Location = new System.Drawing.Point(161, 352);
            this.outputGroupBox.Name = "outputGroupBox";
            this.outputGroupBox.Size = new System.Drawing.Size(830, 197);
            this.outputGroupBox.TabIndex = 9;
            this.outputGroupBox.TabStop = false;
            this.outputGroupBox.Text = "Окно вывода";
            this.outputGroupBox.MouseCaptureChanged += new System.EventHandler(this.OutputGroupBox_MouseCaptureChanged);
            // 
            // outputTextBox
            // 
            this.outputTextBox.BackColor = System.Drawing.SystemColors.Window;
            this.outputTextBox.Font = new System.Drawing.Font("Segoe UI", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.outputTextBox.Location = new System.Drawing.Point(96, 22);
            this.outputTextBox.Multiline = true;
            this.outputTextBox.Name = "outputTextBox";
            this.outputTextBox.ReadOnly = true;
            this.outputTextBox.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.outputTextBox.Size = new System.Drawing.Size(638, 161);
            this.outputTextBox.TabIndex = 0;
            // 
            // scriptParametersGroupBox
            // 
            this.scriptParametersGroupBox.Controls.Add(this.selectResultDirectoryButton);
            this.scriptParametersGroupBox.Controls.Add(this.selectSecondFileButton);
            this.scriptParametersGroupBox.Controls.Add(this.secondFilePathLabel);
            this.scriptParametersGroupBox.Controls.Add(this.resultDirectoryLabel);
            this.scriptParametersGroupBox.Controls.Add(this.secondFilePathTextBox);
            this.scriptParametersGroupBox.Controls.Add(this.selectFirstFileButton);
            this.scriptParametersGroupBox.Controls.Add(this.resultDirectoryTextBox);
            this.scriptParametersGroupBox.Controls.Add(this.firstFilePathLabel);
            this.scriptParametersGroupBox.Controls.Add(this.firstFilePathTextBox);
            this.scriptParametersGroupBox.Controls.Add(this.selectPythonButton);
            this.scriptParametersGroupBox.Controls.Add(this.pythonPathLabel);
            this.scriptParametersGroupBox.Controls.Add(this.pythonPathTextBox);
            this.scriptParametersGroupBox.Location = new System.Drawing.Point(161, 32);
            this.scriptParametersGroupBox.Name = "scriptParametersGroupBox";
            this.scriptParametersGroupBox.Size = new System.Drawing.Size(830, 270);
            this.scriptParametersGroupBox.TabIndex = 2;
            this.scriptParametersGroupBox.TabStop = false;
            this.scriptParametersGroupBox.Text = "Параметры скрипта";
            this.scriptParametersGroupBox.MouseCaptureChanged += new System.EventHandler(this.ScriptParametersGroupBox_MouseCaptureChanged);
            // 
            // selectResultDirectoryButton
            // 
            this.selectResultDirectoryButton.Location = new System.Drawing.Point(660, 220);
            this.selectResultDirectoryButton.Name = "selectResultDirectoryButton";
            this.selectResultDirectoryButton.Size = new System.Drawing.Size(75, 23);
            this.selectResultDirectoryButton.TabIndex = 11;
            this.selectResultDirectoryButton.Text = "Выбрать";
            this.selectResultDirectoryButton.UseVisualStyleBackColor = true;
            this.selectResultDirectoryButton.Click += new System.EventHandler(this.SelectResultDirectoryButton_Click);
            // 
            // selectSecondFileButton
            // 
            this.selectSecondFileButton.Location = new System.Drawing.Point(659, 162);
            this.selectSecondFileButton.Name = "selectSecondFileButton";
            this.selectSecondFileButton.Size = new System.Drawing.Size(75, 23);
            this.selectSecondFileButton.TabIndex = 8;
            this.selectSecondFileButton.Text = "Выбрать";
            this.selectSecondFileButton.UseVisualStyleBackColor = true;
            this.selectSecondFileButton.Click += new System.EventHandler(this.SelectSecondFileButton_Click);
            // 
            // secondFilePathLabel
            // 
            this.secondFilePathLabel.AutoSize = true;
            this.secondFilePathLabel.Location = new System.Drawing.Point(96, 165);
            this.secondFilePathLabel.Name = "secondFilePathLabel";
            this.secondFilePathLabel.Size = new System.Drawing.Size(137, 15);
            this.secondFilePathLabel.TabIndex = 7;
            this.secondFilePathLabel.Text = "Путь до второго файла:";
            // 
            // resultDirectoryLabel
            // 
            this.resultDirectoryLabel.AutoSize = true;
            this.resultDirectoryLabel.Location = new System.Drawing.Point(97, 223);
            this.resultDirectoryLabel.Name = "resultDirectoryLabel";
            this.resultDirectoryLabel.Size = new System.Drawing.Size(155, 15);
            this.resultDirectoryLabel.TabIndex = 10;
            this.resultDirectoryLabel.Text = "Директория под результат:";
            // 
            // secondFilePathTextBox
            // 
            this.secondFilePathTextBox.Location = new System.Drawing.Point(258, 162);
            this.secondFilePathTextBox.Name = "secondFilePathTextBox";
            this.secondFilePathTextBox.Size = new System.Drawing.Size(376, 23);
            this.secondFilePathTextBox.TabIndex = 6;
            // 
            // selectFirstFileButton
            // 
            this.selectFirstFileButton.Location = new System.Drawing.Point(659, 104);
            this.selectFirstFileButton.Name = "selectFirstFileButton";
            this.selectFirstFileButton.Size = new System.Drawing.Size(75, 23);
            this.selectFirstFileButton.TabIndex = 5;
            this.selectFirstFileButton.Text = "Выбрать";
            this.selectFirstFileButton.UseVisualStyleBackColor = true;
            this.selectFirstFileButton.Click += new System.EventHandler(this.SelectFirstFileButton_Click);
            // 
            // resultDirectoryTextBox
            // 
            this.resultDirectoryTextBox.Location = new System.Drawing.Point(258, 220);
            this.resultDirectoryTextBox.Name = "resultDirectoryTextBox";
            this.resultDirectoryTextBox.Size = new System.Drawing.Size(377, 23);
            this.resultDirectoryTextBox.TabIndex = 9;
            // 
            // firstFilePathLabel
            // 
            this.firstFilePathLabel.AutoSize = true;
            this.firstFilePathLabel.Location = new System.Drawing.Point(96, 107);
            this.firstFilePathLabel.Name = "firstFilePathLabel";
            this.firstFilePathLabel.Size = new System.Drawing.Size(138, 15);
            this.firstFilePathLabel.TabIndex = 4;
            this.firstFilePathLabel.Text = "Путь до первого файла:";
            // 
            // firstFilePathTextBox
            // 
            this.firstFilePathTextBox.Location = new System.Drawing.Point(258, 104);
            this.firstFilePathTextBox.Name = "firstFilePathTextBox";
            this.firstFilePathTextBox.Size = new System.Drawing.Size(376, 23);
            this.firstFilePathTextBox.TabIndex = 3;
            // 
            // selectPythonButton
            // 
            this.selectPythonButton.Location = new System.Drawing.Point(659, 46);
            this.selectPythonButton.Name = "selectPythonButton";
            this.selectPythonButton.Size = new System.Drawing.Size(75, 23);
            this.selectPythonButton.TabIndex = 2;
            this.selectPythonButton.Text = "Выбрать";
            this.selectPythonButton.UseVisualStyleBackColor = true;
            this.selectPythonButton.Click += new System.EventHandler(this.SelectPythonButton_Click);
            // 
            // pythonPathLabel
            // 
            this.pythonPathLabel.AutoSize = true;
            this.pythonPathLabel.Location = new System.Drawing.Point(96, 49);
            this.pythonPathLabel.Name = "pythonPathLabel";
            this.pythonPathLabel.Size = new System.Drawing.Size(96, 15);
            this.pythonPathLabel.TabIndex = 1;
            this.pythonPathLabel.Text = "Путь до Питона:";
            // 
            // pythonPathTextBox
            // 
            this.pythonPathTextBox.Location = new System.Drawing.Point(258, 46);
            this.pythonPathTextBox.Name = "pythonPathTextBox";
            this.pythonPathTextBox.Size = new System.Drawing.Size(376, 23);
            this.pythonPathTextBox.TabIndex = 0;
            // 
            // MainWindowForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1178, 624);
            this.Controls.Add(this.mainPanel);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.MinimumSize = new System.Drawing.Size(1194, 663);
            this.Name = "MainWindowForm";
            this.Text = "Соединитель .lsr";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.MainForm_FormClosing);
            this.SizeChanged += new System.EventHandler(this.MainWindowForm_SizeChanged);
            this.mainPanel.ResumeLayout(false);
            this.outputGroupBox.ResumeLayout(false);
            this.outputGroupBox.PerformLayout();
            this.scriptParametersGroupBox.ResumeLayout(false);
            this.scriptParametersGroupBox.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private Panel mainPanel;
        private Button startButton;
        private GroupBox outputGroupBox;
        private TextBox outputTextBox;
        private GroupBox scriptParametersGroupBox;
        private Button selectSecondFileButton;
        private Label secondFilePathLabel;
        private TextBox secondFilePathTextBox;
        private Button selectFirstFileButton;
        private Label firstFilePathLabel;
        private TextBox firstFilePathTextBox;
        private Button selectPythonButton;
        private Label pythonPathLabel;
        private TextBox pythonPathTextBox;
        private Button selectResultDirectoryButton;
        private Label resultDirectoryLabel;
        private TextBox resultDirectoryTextBox;
    }
}