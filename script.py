import biketrauma_FOUX

df = biketrauma_FOUX.Load_db().save_as_df()
biketrauma_FOUX.plot_location(biketrauma_FOUX.get_accident(df))
