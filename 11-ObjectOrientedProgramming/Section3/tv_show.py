# tv_show.py file
# main program
import tv as lib

def main():
   # object creation
   tv1 = lib.tv()

   # object usage
   tv1.show_status()
   tv1.toggle_on()
   tv1.show_status()
   tv1.toggle_on()
   tv1.show_status()

if __name__ == "__main__":
   main() 