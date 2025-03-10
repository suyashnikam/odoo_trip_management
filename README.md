# odoo_trip_management

Setup document and installation procedure

(According to Mac OS)

Step 1: Open terminal Navigate to path where you want your project to setup
>> cd desktop

Step 2: Cloning odoo 17.0 CE
>> git clone -b 17.0 --single-branch --depth=1 https://github.com/odoo/odoo.git

Step 3: Setup Virtual Environment
>> cd odoo
>> python3.11 -m venv odoo17env

Step 4: Activate the virtual Environment
>> source odoo17env/bin/activate

Step 5: Install Wheel separately
>> python -m pip install wheel
>> pip install --upgrade pip

Step 6: Install other requirements now
>> python -m pip install -r requirements.txt

Step 7: Start the PostgreSQL 14 database server as a background service on macOS
>> brew services start postgresql

Step 8: Start the Odoo server
python odoo-bin --addons-path addons,odoo/addons

Step 9: Stopping the Odoo server
>> ctrl + c

Step 10: Start the Odoo server with creating database
>>python odoo-bin --addons-path addons,odoo/addons -d odoo17

Navigate to browser > Now select odoo17 DB > Login to odoo using user : admin & pass: admin

Step 11: Move module directory to the addons path (For now going with addons, or else we can
go with custom addons, by adding custom addons path in conf.)

Step 12 : Install the trip management module
Navigate to app module > Update the app list > search for trip > install the trip management module.

Step 13: Create Trip
Navigate to inventory module > under operation > submenu as trips > Create trip and update trip
using wizard > select a record in list view and download report.
