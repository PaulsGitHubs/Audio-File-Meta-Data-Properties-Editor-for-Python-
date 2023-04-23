import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QTextEdit
from mutagen import File


class AudioEditor(QWidget):
    def __init__(self):
        super(AudioEditor, self).__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.path_label = QLabel('Audio File:')
        self.path_input = QLineEdit()
        self.browse_button = QPushButton('Browse')

        self.artist_label = QLabel('Artist:')
        self.artist_input = QLineEdit()

        self.title_label = QLabel('Title:')
        self.title_input = QLineEdit()

        self.album_label = QLabel('Album:')
        self.album_input = QLineEdit()

        self.genre_label = QLabel('Genre:')
        self.genre_input = QLineEdit()

        self.current_metadata_label = QLabel('Current Metadata:')
        self.current_metadata = QTextEdit()
        self.current_metadata.setReadOnly(True)

        self.save_button = QPushButton('Save Changes')

        layout.addWidget(self.path_label)
        layout.addWidget(self.path_input)
        layout.addWidget(self.browse_button)
        layout.addWidget(self.artist_label)
        layout.addWidget(self.artist_input)
        layout.addWidget(self.title_label)
        layout.addWidget(self.title_input)
        layout.addWidget(self.album_label)
        layout.addWidget(self.album_input)
        layout.addWidget(self.genre_label)
        layout.addWidget(self.genre_input)
        layout.addWidget(self.current_metadata_label)
        layout.addWidget(self.current_metadata)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

        self.browse_button.clicked.connect(self.browse_file)
        self.save_button.clicked.connect(self.save_changes)

    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open audio file', '', 'Audio Files (*.mp3 *.flac *.m4a *.ogg *.opus *.wav);;All Files (*)')
        if file_path:
            self.path_input.setText(file_path)
            self.load_file(file_path)

    def load_file(self, file_path):
        self.audio_file = File(file_path, easy=True)

        self.artist_input.setText(self.audio_file.get('artist', [''])[0])
        self.title_input.setText(self.audio_file.get('title', [''])[0])
        self.album_input.setText(self.audio_file.get('album', [''])[0])
        self.genre_input.setText(self.audio_file.get('genre', [''])[0])

        self.display_current_metadata()

    def display_current_metadata(self):
        current_metadata = "Artist: {}\nTitle: {}\nAlbum: {}\nGenre: {}".format(
            self.artist_input.text(),
            self.title_input.text(),
            self.album_input.text(),
            self.genre_input.text()
        )
        self.current_metadata.setPlainText(current_metadata)

    def save_changes(self):
        self.audio_file['artist'] = self.artist_input.text()
        self.audio_file['title'] = self.title_input.text()
        self.audio_file['album'] = self.album_input.text()
        self.audio_file['genre'] = self.genre_input.text()

        self.audio_file.save()

        self.display_current_metadata()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AudioEditor()
    window.setWindowTitle('Audio Metadata Editor')
    window.show()
    sys.exit(app.exec_())
