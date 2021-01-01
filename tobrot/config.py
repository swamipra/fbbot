from tobrot.sample_config import Config

#Fill your all data, read readme for reference

#FOR CUSTOM COMMANDS READ REAME AND FILL THEM...

class Config(Config):
    TG_BOT_TOKEN= "1322090312:AAH2cJIjL_RKnp8gCJ1ktUbM3Q_q7dz-Phs"
    APP_ID = 1555221
    API_HASH = "30ac4b652eb9a467f9c7235840da9e64"
    OWNER_ID = 576110845
    AUTH_CHANNEL = [-1001415709202]
    DESTINATION_FOLDER = "lol" #Name of your folder read readme(not id of the folder)
    #fill your rclone config like this(Your config may have some extra value or less. so Don't worry)
    # Do not delete [DRIVE] #do not delete [DRIVE] but replace remaining part
    RCLONE_CONFIG = """
type = drive
client_id = 280571306215-7dmicnbtjrjmh143nqmvrvtidn4525vo.apps.googleusercontent.com
client_secret = t869gff56gKQRW0ZNlNChuPe
scope = drive
token = {"access_token":"ya29.a0AfH6SMBEWFcxP5asQec6iQiUkQOYGbShKaXYtui-EQvoHviDlilQ3a0Wxzu4LYmNNVC85P-jyCnjhpKK0rsZL70Tx3VHACOjOjmL1NhHlXxUseXG-2Rusn2Fga4RjoS6412gEUx9WsSLNleV5nZwl0_nwtzokoCI1d9zfG_Mn-Q","token_type":"Bearer","refresh_token":"1//0go1u69L3pUIaCgYIARAAGBASNwF-L9Irf1HrCP2hPO1LnTOCX51K-yFxjVH-fz5aFPhRdNxGVih2HUdfixBAuwod3TjC03LxyfQ","expiry":"2021-01-01T16:44:17.0101058+05:30"}
team_drive = 0AHprv46iI_QyUk9PVA
root_folder_id =
"""