#!/usr/bin/perl
use strict;
use warnings;

print "Please enter a number: ";
my $number = <STDIN>;
chomp($number);

print "Multiplication table for $number:\n";
for my $i (0..12) {
    my $result = $number * $i;
    print "$number x $i = $result\n";
}