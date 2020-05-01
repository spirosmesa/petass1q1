package com.petAss1.mixnet;

import org.bouncycastle.jce.provider.BouncyCastleProvider;

import java.security.Security;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args ) {
        Security.addProvider(new BouncyCastleProvider());
    }
}
