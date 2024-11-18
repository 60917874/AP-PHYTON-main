package ui;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.text.SimpleDateFormat;
import java.util.Date;

public class Login extends JFrame {
    private static final long serialVersionUID = 1L;

    private JTextField idOperadorField;
    private JPasswordField passwordField;
    private boolean isIdFieldFocused = true;

    private JLabel dateLabel;
    private JLabel timeLabel;

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            Login login = new Login();
            login.setVisible(true);
        });
    }

    public Login() {
        setTitle("Ace Home Center");
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setSize(600, 400);
        setLocationRelativeTo(null);
        setLayout(new BorderLayout());

        JPanel leftPanel = new JPanel(new GridBagLayout());
        leftPanel.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));
        leftPanel.setBackground(new Color(171, 39, 39));

        JPanel imagePanel = new JPanel();
        imagePanel.setLayout(new FlowLayout(FlowLayout.CENTER, 10, 10));
        imagePanel.setBackground(new Color(171, 39, 39)); 
        JLabel imagenLabel = new JLabel();
        ImageIcon icono = new ImageIcon(getClass().getResource("/ui/img/acehomecenter.png"));
        Image imagenEscalada = icono.getImage().getScaledInstance(460, 360, Image.SCALE_SMOOTH); 
        imagenLabel.setIcon(new ImageIcon(imagenEscalada));
        imagePanel.add(imagenLabel);
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(5, 5, 5, 5);

        JPanel spacePanel = new JPanel();
        spacePanel.setPreferredSize(new Dimension(0, 100));
        leftPanel.add(spacePanel, gbc);

        gbc.gridx = 0; 
        gbc.gridy = 1;
        gbc.anchor = GridBagConstraints.WEST;
        JLabel idLabel = new JLabel("ID Operador:");
        idLabel.setForeground(Color.WHITE);
        leftPanel.add(idLabel, gbc);

        gbc.gridx = 1;
        idOperadorField = new JTextField(10);
        idOperadorField.addFocusListener(new java.awt.event.FocusAdapter() {
            public void focusGained(java.awt.event.FocusEvent evt) {
                isIdFieldFocused = true;
            }
        });
        idOperadorField.addActionListener(e -> {
            if (idOperadorField.getText().length() == 6) {
                passwordField.requestFocus();
            }
        });
        leftPanel.add(idOperadorField, gbc);

        gbc.gridx = 0; 
        gbc.gridy = 2; 
        JLabel passLabel = new JLabel("Contraseña:");
        passLabel.setForeground(Color.WHITE);
        leftPanel.add(passLabel, gbc);

        gbc.gridx = 1; 
        passwordField = new JPasswordField(10);
        passwordField.addFocusListener(new java.awt.event.FocusAdapter() {
            public void focusGained(java.awt.event.FocusEvent evt) {
                isIdFieldFocused = false;
            }
        });
        passwordField.addActionListener(e -> login());
        leftPanel.add(passwordField, gbc);

        add(leftPanel, BorderLayout.WEST);

        JPanel rightPanel = new JPanel(new GridLayout(4, 4, 10, 10));
        rightPanel.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));
        rightPanel.setBackground(new Color(171, 39, 39));

        String[] buttons = {
            "1", "2", "3", "Cancelar",
            "4", "5", "6", "Borrar",
            "7", "8", "9", "Atrás",
            "", "0", "", "Enter"
        };

        for (String text : buttons) {
            JButton button = new JButton(text);
            if (!text.isEmpty()) {
                button.addActionListener(new KeypadListener());
                button.setBackground(new Color(236, 236, 236));
                button.setForeground(Color.BLACK);

                button.addMouseListener(new java.awt.event.MouseAdapter() {
                    public void mouseEntered(java.awt.event.MouseEvent evt) {
                        button.setBackground(new Color(173, 171, 171));
                    }

                    public void mouseExited(java.awt.event.MouseEvent evt) {
                        button.setBackground(new Color(236, 236, 236));
                    }
                });
            } else {
                button.setEnabled(false);
            }
            rightPanel.add(button);
        }

        add(rightPanel, BorderLayout.CENTER);

        JPanel bottomPanel = new JPanel();
        bottomPanel.setBackground(new Color(171, 39, 39));
        bottomPanel.setLayout(new BorderLayout());

        timeLabel = new JLabel();
        timeLabel.setForeground(Color.WHITE);
        timeLabel.setHorizontalAlignment(SwingConstants.LEFT);
        bottomPanel.add(timeLabel, BorderLayout.WEST);

        dateLabel = new JLabel();
        dateLabel.setForeground(Color.WHITE);
        dateLabel.setHorizontalAlignment(SwingConstants.CENTER);
        bottomPanel.add(dateLabel, BorderLayout.CENTER);

        add(bottomPanel, BorderLayout.SOUTH);

        Timer timer = new Timer(1000, new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                updateDateTime();
            }
        });
        timer.start();
    }

    private void updateDateTime() {
        Date now = new Date();
        SimpleDateFormat dateFormat = new SimpleDateFormat("dd/MM/yyyy");
        SimpleDateFormat timeFormat = new SimpleDateFormat("HH:mm:ss");

        dateLabel.setText("Fecha: " + dateFormat.format(now));
        timeLabel.setText("Hora: " + timeFormat.format(now));
    }

    private void login() {
        String idOperador = idOperadorField.getText();
        String password = new String(passwordField.getPassword());

        if (idOperador.equals("123456") && password.equals("123456")) {
            JOptionPane.showMessageDialog(this, "Has ingresado correctamente", "Login", JOptionPane.INFORMATION_MESSAGE);
        } else {
            JOptionPane.showMessageDialog(this, "El ID o la Contraseña no coinciden. Inténtalo nuevamente.", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void clearFields() {
        idOperadorField.setText("");
        passwordField.setText("");
        isIdFieldFocused = true;
        idOperadorField.requestFocus();
    }

    private class KeypadListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            String command = e.getActionCommand();

            if (command.equals("Borrar")) {
                if (isIdFieldFocused) {
                    idOperadorField.setText("");
                } else {
                    passwordField.setText("");
                }
            } else if (command.equals("Atrás")) {
                if (isIdFieldFocused) {
                    String currentText = idOperadorField.getText();
                    if (currentText.length() > 0) {
                        idOperadorField.setText(currentText.substring(0, currentText.length() - 1));
                    }
                } else {
                    char[] currentPassword = passwordField.getPassword();
                    if (currentPassword.length > 0) {
                        String updatedPassword = new String(currentPassword).substring(0, currentPassword.length - 1);
                        passwordField.setText(updatedPassword);
                    }
                }
            } else if (command.equals("Cancelar")) {
                clearFields();
            } else if (command.equals("Enter")) {
                if (isIdFieldFocused && idOperadorField.getText().length() == 6) {
                    passwordField.requestFocus();
                } else if (!isIdFieldFocused && passwordField.getPassword().length > 0) {
                    login();
                }
            } else {
                if (isIdFieldFocused) {
                    String currentText = idOperadorField.getText();
                    if (currentText.length() < 6) {
                        idOperadorField.setText(currentText + command);
                    }
                } else {
                    char[] currentPassword = passwordField.getPassword();
                    if (currentPassword.length < 6) {
                        passwordField.setText(new String(currentPassword) + command);
                    }
                }
            }
        }
    }
}
