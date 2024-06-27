import logging as log

log.basicConfig(level=log.DEBUG,
                format="%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s",
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler("capa_datos.log"),
                    log.StreamHandler()

                ])

if __name__ == "__main__":
    log.debug("Mensaje a nivel DEBUG")
    log.info("mensaje a nivel de INFO")
    log.warning("mensaje a nivel de WARNING")
    log.error("mensaje a nivel ERROR")
    log.critical("mensaje a nivel CRITICO")

