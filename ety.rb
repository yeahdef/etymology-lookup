#!/usr/bin/env ruby

require 'open-uri'
require 'nokogiri'
 
q = ARGV[0]
uri = "http://www.etymonline.com/index.php?term="+q
html = Nokogiri::HTML(open(uri))

result = html.css('dt').each do |node| 
	puts ""
	puts node.text
	puts node.next_element.text
end
