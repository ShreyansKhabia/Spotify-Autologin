# Spotify Autologin

This script opens a VPN, logs into spotify with your credentials and then closes the VPN.

this is very useful if you have set your spotify country different from where you live (as I have done because many artists are only available on Spotify in certain regions), as you can only use a Spotify account in a different country or region for up to 14 days, before asking to login again form your accounts spotify country.

## required library/software
<p>software:  

        VPN: Psiphon3 (you can modify the code to open VPN of your choice)
</p>

<p>libraries:

        selenium  
        time  
        datetime  
        os
</p>



#### note:

preset the country you want to login from in Psiphon3

if an error occurs, update the class name of the Login Button in the code using inspect element in your browser(see comment in the code).  
PS: this is a rare event.
