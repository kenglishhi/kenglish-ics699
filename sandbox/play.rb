#!/usr/bin/ruby
#
puts "array"

def do_dispatch
  (0..9).each do | i|
    puts "thread 1"
    do_work
  end 
end
def do_work
  sleep rand(10)
end
do_dispatch
