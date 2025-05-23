package com.example;

public class MailUtil {
    public static boolean isValidEmail(String email) {
        return email != null && email.contains("@");
    }
}
