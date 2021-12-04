import os
import sys
import winreg as reg
'''
README
This is working example to add popup box into your right click menu.
Please run this script with substituting proper values to match your desired effect!
To modify windows registry, you need to run it with administrator rights! 
Use at your own risk : )
'''

class KeyManager:
    ##### MODIFY FREELY
    script_path = f" {os.getcwd()}\\TypicalWindow.py"
    context_menu_name = "Popup box!"

    # Choose proper key root:
    # HKEY_CLASSES_ROOT sets key for all users
    # HKEY_CURRENT_USER sets key only for current user.
    # in most cases, it shuld suffice to use HKEY_CURRENT_USER
    key_root = reg.HKEY_CURRENT_USER
    # File extension that you use must have "shell" in path to make it work
    subkey_path = r"SOFTWARE\\Classes\\*\\shell\\unpack_logs"
    ##### EOF MODIFY FREELY
    
    python_exe = sys.executable
    python_exe_hidden_term = '\\'.join(python_exe.split('\\')[:-1])+"\\pythonw.exe"
    executed_command = python_exe_hidden_term + script_path

    def __getOuterAndInnerKey(self):
        outer_key = reg.CreateKeyEx(self.key_root, self.subkey_path)
        inner_key = reg.CreateKeyEx(outer_key, r"command")
        return outer_key, inner_key

    def install_key(self):
        # name of button appearing in context menu
        outer_key, inner_key = self.getOuterAndInnerKey()
        reg.SetValue(outer_key, '', reg.REG_SZ, self.context_menu_name)
        reg.SetValue(inner_key, '', reg.REG_SZ, self.executed_command)
        print(f"Script successfully added {self.executed_command} to right click menu.")

    def uninstall_key(self):
        outer_key, inner_key = self.__getOuterAndInnerKey() 
        # important! reversed order
        try:
            reg.DeleteKeyEx(outer_key, r"command")
            print("Registry key successfully deleted.")
        except FileNotFoundError:
            print(f"Cannot find key under {inner_key}\command. Wrong key path?")
        try:
            reg.DeleteKeyEx(self.key_root, self.subkey_path)
            print("Registry key successfully deleted.")
        except FileNotFoundError:
            print(f"Cannot find key under {self.key_root}\{self.subkey_path}. Wrong key path?")
        

def main():
    k = KeyManager()
    #k.install_key()
    k.uninstall_key()


if __name__ == "__main__":
    main()