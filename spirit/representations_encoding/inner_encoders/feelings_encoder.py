def encode_feelings(feelings, _, snapshot):
    snapshot.feelings.hunger = feelings.hunger
    snapshot.feelings.thirst = feelings.thirst
    snapshot.feelings.exhaustion = feelings.exhaustion
    snapshot.feelings.happiness = feelings.happiness


encode_feelings.field = "RepresentationFeelings"
