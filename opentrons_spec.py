from opentrons import containers, instruments, robot

#Set working environment.
trough = containers.load('trough-12row','A1')
p1000rack = containers.load('tiprack-1000ul','A2')
p200rack = containers.load('tiprack-200ul','A3')
plate1 = containers.load('96-flat','B1')
plate2 = containers.load('96-flat','B2')
trash = containers.load('point','B3')

p300_multi = instruments.Pipette(
	axis = 'b',
	max_volume=300,
	trash_container=trash,
	tip_racks=[p1000rack],     #1000 uL tiprack for the 300uL pipette, as this is the equipment available.
	channels=8
	)

p200 = instruments.Pipette(
	axis = 'b',
	max_volume=200,
	trash_container=trash,
	tip_racks=[p200rack]
	)

#Use multi-channel pipette to transfer 200 uL of Solution A from Trough A into wells A1-H1, A2-H2 of Plate 1. 
p300_multi.transfer(
    200,
    trough.wells('A1'),
    plate1.wells('A1', to='H2'),
    new_tip='never'
)

#Dispose of tips in trash.

p300_multi.drop_tip()

#Update these transfer volumes as necessary.
transfer_volumes = [20,25,30,35,40,45,50,55]

#Use single channel pipette to add 20 - 55 uL (in 5 uL increments) of Trough A1 to Plate 1 wells A1-H1.
p200.transfer(
    transfer_volumes,
    trough.wells('A1'),
    plate1.wells('A1', to='H1'),
    new_tip='always'             #May not be necessary, but not specified in spec.
)


#Use single channel pipette to add 20 - 55 uL (in 5 uL increments) of Trough A5 to Plate 1 wells A2-H2.
p200.transfer(
    transfer_volumes,
    trough.wells('A5'),
    plate1.wells('A2', to='H2'),
    new_tip='always'
)

#Delay 30 minutes.

p300_multi.delay(minutes=30)

#Move all solutions from Plate 1 wells A1-H2 to Plate 2 wells A1-H2.

p300_multi.transfer(
    300,
    plate1.wells('A1', to='H1'),
    plate2.wells('A1', to='H1')
)

p300_multi.transfer(
    300,
    plate1.wells('A2', to='H2'),
    plate2.wells('A2', to='H2')
)

#View robot commands.
for c in robot.commands():
    print(c)