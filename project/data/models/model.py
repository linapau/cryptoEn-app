from django.db import models

class FileModel(models.Model):
    fileID = models.CharField(max_length=255)
    fileName = models.CharField(max_length=255)
    fileSize = models.FloatField()
    encryptionStatus = models.BooleanField(default=False)

#     def encryptionFile(self):
#        # Implement encryption logic here
#        pass
#
#    def decryptionFile(self):
#        # Implement decryption logic here
#        pass

    def upload(self):
        # Implement file upload logic here
        pass

    def download(self):
        # Implement file download logic here
        pass

    def __str__(self):
        return self.fileName
    