# pikachu
MTG-sorter project for Canadians

## Instructions
1. Clone the repo to the raspberry to the /opt dir

    ``cd /opt``

    ``git clone https://github.com/RevoltBI/pikachu.git``
   
    ``cd pikachu``
2. Install python packages
    ```sh
    poetry install
    ```

3. Activate poetry environment

    1. Use virtual environment in shell
        linux/osx:      
        ```sh
        source /home/pi/.cache/pypoetry/virtualenvs/pikachu*/bin/activate
        ```

4. Set up some variables like `pin` and ``interval`` in src/configuration/config.cfg

    `pin` is GPIO pin that is connected to the device
   
    `interval` is the command frequency in seconds 
    ```sh
    pin = 14
    interval = 0.5
    ```

5. Run the program
    ```shell
   python3 src/main.py
   ```
