#!/usr/bin/env ruby
puts ARGV[0].scan(/(?<=from:)[^\]]{1,}|(?<=to:)[^\]]{1,}|(?<=flags:)[^\]]{1,}/).join(",")

