from django.core.management.commands import makemessages
import shutil
import os


class Command(makemessages.Command):
    def folder_to_folder(self, root_src_dir, root_dst_dir, method):
        for src_dir, dirs, files in os.walk(root_src_dir):
            dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
            if not os.path.exists(dst_dir):
                os.makedirs(dst_dir)
            for file_ in files:
                src_file = os.path.join(src_dir, file_)
                dst_file = os.path.join(dst_dir, file_)
                if os.path.exists(dst_file):
                    os.remove(dst_file)

                if method == 'move':
                    shutil.move(src_file, dst_dir)
                else:
                    shutil.copy(src_file, dst_dir)
        if method == 'move':
            shutil.rmtree(root_src_dir)

    def handle(self, *args, **options):
        root_src_dir = '/src/locale/'
        root_dst_dir = '/data/locale/'

        self.folder_to_folder(root_dst_dir, root_src_dir, 'copy')
        super(Command, self).handle(*args, **options)
        self.folder_to_folder(root_src_dir, root_dst_dir, 'move')
