from crontab import CronTab
import os 
import shutil

while True:
    def menu():
        print("------------------------------")
        print("1. Agregar Tarea")
        print("2. Listar Tareas")
        print("3. Buscar Tareas")
        print("4. Eliminar Tarea")
        print("5. Finalizar")
        print(" # --> Acceder Manual usuario ")
        print("------------------------------")
    menu()
    opcion = input("Dime una opcion: ")


    def crear_job():
        cron = CronTab(user=input("Usuario del cual quieres eliminar tareas programadas: "))
        for job in cron:
            print("-----------------------------------------------------------------------")
            print("Necesitamos la ruta absoluta de la app o el comando a ejecutar asi que...")
            print("-----------------------------------------------------------------------")

            print("Para volver al Menu pulse 'm'")
            comando = input(" Dime la orden que le vamos a dar al sistema (nombre de la app/comando): ")
            print("-----------------------------------------------------------------------")
            if comando == "m" and "M":
                break
            ruta = shutil.which(comando)

            if ruta:
                apcom = input("¿Es una app o un comando? --> ")

            else:
                print("El comando/app especificada no existe dentro del sistema.")
                return
            print("-----------------------------------------------------------------------")
            comentario = input(" Indicame el comentario que le vamos a agregar a la tarea --> ")
            print("-----------------------------------------------------------------------")

            print("###########ADVERTENCIA###########")
            print("SI NO QUIERES INDICAR NINGUN MINUTO,HORA,DIA DE MES, DIA SEMANAL. PULSE INTRO SIN INDICAR NINGUN PARAMETRO")

            minuto = input("Minuto (0-60): ")
            
            hora = input("Hora (0-23): ")

            dia_mes = input("Mes (0-31): ")

            mes = input("Mes (0-12 )")

            semana = input("Semana (0-7 ): ")

            if apcom == "comando":
                duda = input("¿Es necesario indicar algun parametro/ruta al comando? (yes/no): ")
                if duda == "yes":
                    parametro = input("Indica el parametro o la ruta (Debes incluir todo aqui, todos los parametros/rutas en el orden correcto --> ")
                    job = cron.new(
                    
                    command = f"{comando} {parametro}  ",

                    comment = f"{comentario}"
                )
                    job.setall(f'{minuto} {hora} {dia_mes} {mes} {semana}')

                    linea_cron = f"{minuto} {hora} {dia_mes} {mes} {semana} {comando} {parametro}"

                    print("\nCron generado:")
                    print(linea_cron)

                    confirmar = input("\n¿Añadir al crontab? (s/n): ")

                    if confirmar == "s" or "si":
                        cron.write()

                        print("Tarea agregada al crontab del usuario")
                    else:
                        print("Esta bien, cerrando programa...")
                        return
                elif duda == "no":
                    job = cron.new(
                    
                    command = f"{comando}  ",

                    comment = f"{comentario}"
                )

                    job.setall(f'{minuto} {hora} {dia_mes} {mes} {semana}')
                    
                    linea_cron = f"{minuto} {hora} {dia_mes} {mes} {semana} {comando} "

                    print("\nCron generado:")
                    print(linea_cron)

                    confirmar = input("\n¿Añadir al crontab? (s/n): ")

                    if confirmar == "s" or "si":
                        cron.write()

                        print("Tarea agregada al crontab del usuario")
                    else:
                        print("Esta bien, cerrando programa...")
                        return
                    cron.write()


                elif duda != "yes" or "no":
                    print("opcion no valida")
                    return
            if apcom == "app":

                job = cron.new(

                command = f"{comando}  ",

                comment = f"{comentario}"

            )
                job.setall(f'{minuto} {hora} {dia_mes} {mes} {semana}')
                linea_cron = f"{minuto} {hora} {dia_mes} {mes} {semana} {comando} "
                
                print("\nCron generado:")
                print(linea_cron)

                confirmar = input("\n¿Añadir al crontab? (s/n): ")

                if confirmar == "s" or "si":
                    cron.write()

                    print("Tarea agregada al crontab del usuario")
                else:
                    print("Esta bien, cerrando programa...")
                    return 
                cron.write()


                print("Tarea agregada al crontab del usuario")


    if opcion == "1" :
        crear_job()

    def eliminar_job():
        cron = CronTab(user=input("Usuario del cual quieres eliminar tareas programadas: "))
        comentari = input("Dime un comentario de una tarea para eliminarla: ")

        for job in cron:
            if comentari == job.comment  :
                print(job)
                while True:
                    confirma = input("¿Esta seguro de que quiere eliminar las tareas mostradas (yes/no)? :") 

                    if confirma == "yes":

                        cron.remove(job)
                        cron.write()
                        print("Tarea eliminada correctamente")

                        return
                    elif confirma == "no":
                        print("Volviendo al menu")
                        return                    
                    elif confirma != "yes" or "no":
                        print("opción no valida")
                        return                
                    
    if opcion == "4":
        eliminar_job()

    def lista_tareas():
        cron = CronTab(user=input("Usuario del cual quieres ver su listado de tareas programadas: "))
        print("-----------------------")
        print("listado de tareas: ")
        for jobs in cron:
            print("---------------")
            print(jobs)
            input("presiona enter para continuar...")
    if opcion == "2":
        lista_tareas()


    def buscar_job():
        cron = CronTab(user=input("Usuario en el cual quieres buscar tareas programadas: "))

        comentari = input("Dime un comentario ( o parte del comentario )de una tarea para buscar: ")
        
        for job in cron:
            if comentari.lower() in job.comment.lower():
                print("Tarea: ", job)
    if opcion == "3":
        buscar_job()

    if opcion == "5":
        print("Saliendo del programa...")
        break



