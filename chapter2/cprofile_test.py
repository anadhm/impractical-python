"""Profile the palingrams module with cProfile."""
import cProfile
import palingrams1
cProfile.run('palingrams1.find_palingrams()')