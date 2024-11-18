package ui;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Collections;
import java.util.List;
import java.util.ArrayList;

public class Login extends JFrame {
    private static final long serialVersionUID = 1L;
    private JPasswordField passwordd;
    private StringBuilder password = new StringBuilder();
    private int intentosFallidos = 0;
    private boolean bloqueado = false;

    public static void main(String[] args) {
        EventQueue.invokeLater(() -> {
            try {
            	Login frame = new Login();
                frame.setVisible(true);
            } catch (Exception e) {
                e.printStackTrace();
            }
        });
    }

    public Login() {
        setTitle("Login");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setBounds(100, 100, 320, 845);
        setLayout(null);
        setLocationRelativeTo(null);
        setResizable(false);
        getContentPane().setBackground(new Color(128, 0, 128));
        
        JLabel imagenLabel = new JLabel();
        imagenLabel.setBounds(55, 350, 200, 680); 
        ImageIcon icono = new ImageIcon(getClass().getResource("/uiimg/yape.png"));
        Image imagen = icono.getImage().getScaledInstance(200, 150, Image.SCALE_SMOOTH); 
        imagenLabel.setIcon(new ImageIcon(imagen));
        getContentPane().add(imagenLabel);
        
        JLabel nuevaImagenLabel = new JLabel();
        nuevaImagenLabel.setBounds(55, 50, 200, 170);
        ImageIcon nuevaImagenIcono = new ImageIcon(getClass().getResource("/uiimg/qr.png"));  
        Image nuevaImagenEscalada = nuevaImagenIcono.getImage().getScaledInstance(200, 150, Image.SCALE_SMOOTH);
        nuevaImagenLabel.setIcon(new ImageIcon(nuevaImagenEscalada));
        getContentPane().add(nuevaImagenLabel);

        passwordd = new JPasswordField();
        passwordd.setBounds(10, 270, 290, 40);
        passwordd.setHorizontalAlignment(SwingConstants.CENTER);
        passwordd.setEditable(false);
        passwordd.setBackground(new Color(224, 191, 234));
        passwordd.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
        getContentPane().add(passwordd);

        JPanel Botones = new JPanel();
        Botones.setBounds(25, 320, 260, 230);
        Botones.setLayout(new GridLayout(4, 3, 5, 5));
        Botones.setBackground(new Color(128, 0, 128));
        getContentPane().add(Botones);

        List<String> botonesList = new ArrayList<>();
        String[] botones = {
            "7", "8", "9",
            "4", "5", "6",
            "1", "2", "3",
                 "0"
        };

        for (String texto : botones) {
            botonesList.add(texto);
        }

        Collections.shuffle(botonesList);

        for (String texto : botonesList) {
            JButton Boton = new JButton(texto);
            Boton.setForeground(Color.BLACK);
            Boton.setFocusPainted(false);
            Boton.setBackground(new Color(224, 191, 234));
            Boton.setBorder(BorderFactory.createLineBorder(new Color(128, 0, 128), 1));
            Boton.setCursor(new Cursor(Cursor.HAND_CURSOR));

            Boton.addActionListener(new LoginActionListener());
            Botones.add(Boton);
        }

        JButton botonBorrar = new JButton("X");
        botonBorrar.setForeground(Color.BLACK);
        botonBorrar.setFocusPainted(false);
        botonBorrar.setBackground(new Color(224, 191, 234));
        botonBorrar.setBorder(BorderFactory.createLineBorder(new Color(200, 200, 200), 1));
        botonBorrar.setCursor(new Cursor(Cursor.HAND_CURSOR));
        botonBorrar.addActionListener(new LoginActionListener());
        Botones.add(botonBorrar);

        JButton btnForgetPassword = new JButton("¿Olvidaste tu contraseña?");
        btnForgetPassword.setBounds(8, 570, 290, 40);
        btnForgetPassword.setBackground(new Color(128, 0, 128));
        btnForgetPassword.setForeground(new Color (255, 255, 255));
        btnForgetPassword.setFocusPainted(false);
        btnForgetPassword.setBorder(BorderFactory.createEmptyBorder());
        btnForgetPassword.setCursor(new Cursor(Cursor.HAND_CURSOR));
        btnForgetPassword.addActionListener(e -> JOptionPane.showMessageDialog(null, "Recuperación de contraseña no disponible."));
        getContentPane().add(btnForgetPassword);
        
        JLabel textoLabel = new JLabel("Hola, yapero");
        textoLabel.setBounds(10, 90, 290, 300);
        textoLabel.setHorizontalAlignment(SwingConstants.CENTER);
        textoLabel.setForeground(new Color(255, 255, 255));
        getContentPane().add(textoLabel);
        
    }

    private class LoginActionListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            if (bloqueado) {
                JOptionPane.showMessageDialog(null, "Acceso bloqueado. Intente nuevamente después de 30 segundos.");
                return;
            }

            String comando = e.getActionCommand();

            if (comando.equals("X")) {
                if (password.length() > 0) {
                    password.setLength(password.length() - 1);
                    passwordd.setText(getCensoredPassword());
                }
                return;
            }

            password.append(comando);
            passwordd.setText(getCensoredPassword());

            if (password.length() == 6) {
                validar();
            }
        }

        private String getCensoredPassword() {
            StringBuilder censoredPassword = new StringBuilder();
            for (int i = 0; i < password.length(); i++) {
                censoredPassword.append('*');
            }
            return censoredPassword.toString();
        }

        private void validar() {
            String claveCorrecta = "123456";
            if (password.toString().equals(claveCorrecta)) {
                JOptionPane.showMessageDialog(null, "¡Bienvenido a Yape!");
                intentosFallidos = 0;
            } else {
                intentosFallidos++;
                if (intentosFallidos >= 3) {
                    bloquearAcceso();
                } else {
                    JOptionPane.showMessageDialog(null, "Contraseña incorrecta. Intenta nuevamente.");
                }
                password.setLength(0);
                passwordd.setText("");
            }
        }

        private void bloquearAcceso() {
            bloqueado = true;
            JOptionPane.showMessageDialog(null, "Acceso bloqueado por demasiados intentos fallidos.");
            Timer timer = new Timer(30000, new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    bloqueado = false;
                    intentosFallidos = 0;
                    JOptionPane.showMessageDialog(null, "Acceso reactivado. Puede intentar nuevamente.");
                }
            });
            timer.setRepeats(false);
            timer.start();
        }
    }
}