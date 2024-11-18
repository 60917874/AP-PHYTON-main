package ui;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class CalculadoraBasica extends JFrame {
    private static final long serialVersionUID = 1L;
    private JTextField Pantalla;
    private double primerNumero = 0;
    private String operador = "";
    private boolean nuevoNumero = true;

    public static void main(String[] args) {
        EventQueue.invokeLater(() -> {
            try {
                CalculadoraBasica frame = new CalculadoraBasica();
                frame.setVisible(true);
            } catch (Exception e) {
                e.printStackTrace();
            }
        });
    }

    public CalculadoraBasica() {
        setTitle("Calculadora");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setBounds(100, 100, 320, 480);
        setLayout(null);
        setLocationRelativeTo(null);
        setResizable(false);

        Pantalla = new JTextField();
        Pantalla.setBounds(10, 10, 290, 60);
        Pantalla.setFont(new Font("Segoe UI", Font.BOLD, 24));
        Pantalla.setHorizontalAlignment(SwingConstants.RIGHT);
        Pantalla.setEditable(false);
        Pantalla.setBackground(new Color(240, 240, 240));
        Pantalla.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
        getContentPane().add(Pantalla);

        JPanel Botones = new JPanel();
        Botones.setBounds(10, 80, 290, 360);
        Botones.setLayout(new GridLayout(6, 4, 5, 5));
        Botones.setBackground(new Color(240, 240, 240));
        getContentPane().add(Botones);

        String[] botones = {
                "%", "CE", "C", "←",
                "1/x", "x²", "√x", "÷",
                "7", "8", "9", "×",
                "4", "5", "6", "-",
                "1", "2", "3", "+",
                "+/-", "0", ".", "="
        };

        for (String texto : botones) {
            JButton boton = new JButton(texto);
            boton.setFont(new Font("Segoe UI", Font.PLAIN, 18));
            boton.setForeground(Color.BLACK);
            boton.setBackground(Color.WHITE);
            boton.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
            boton.setCursor(new Cursor(Cursor.HAND_CURSOR));

            if ("=".equals(texto)) {
                boton.setBackground(new Color(0, 120, 215));
                boton.setForeground(Color.WHITE);
            }

            boton.addActionListener(new CalculadoraActionListener());
            Botones.add(boton);
        }
    }

    private class CalculadoraActionListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            String comando = e.getActionCommand();

            if (comando.equals("C")) {
                Pantalla.setText("");
                operador = "";
                primerNumero = 0;
                nuevoNumero = true;
            } else if (comando.equals("CE")) {
                Pantalla.setText("");
            } else if (comando.equals("=")) {
                calcularResultado();
                operador = "";
                nuevoNumero = true;
            } else if (comando.equals("+/-")) {
                if (!Pantalla.getText().isEmpty()) {
                    double valor = Double.parseDouble(Pantalla.getText());
                    Pantalla.setText(String.valueOf(valor * -1));
                }
            } else if (comando.equals("%")) {
                if (!Pantalla.getText().isEmpty()) {
                    double valor = Double.parseDouble(Pantalla.getText());
                    Pantalla.setText(String.valueOf(valor / 100));
                }
            } else if (comando.equals("1/x")) {
                if (!Pantalla.getText().isEmpty()) {
                    double valor = Double.parseDouble(Pantalla.getText());
                    if (valor != 0) {
                        Pantalla.setText(String.valueOf(1 / valor));
                    }
                }
            } else if (comando.equals("x²")) {
                if (!Pantalla.getText().isEmpty()) {
                    double valor = Double.parseDouble(Pantalla.getText());
                    Pantalla.setText(String.valueOf(Math.pow(valor, 2)));
                }
            } else if (comando.equals("√x")) {
                if (!Pantalla.getText().isEmpty()) {
                    double valor = Double.parseDouble(Pantalla.getText());
                    if (valor >= 0) {
                        Pantalla.setText(String.valueOf(Math.sqrt(valor)));
                    } else {
                        Pantalla.setText("Error");
                    }
                }
            } else if (comando.equals("←")) {
                String textoPantalla = Pantalla.getText();
                if (!textoPantalla.isEmpty()) {
                    Pantalla.setText(textoPantalla.substring(0, textoPantalla.length() - 1));
                }
            } else if (comando.equals("+") || comando.equals("-") || comando.equals("×") || comando.equals("÷")) {
                if (!Pantalla.getText().isEmpty()) {
                    primerNumero = Double.parseDouble(Pantalla.getText());
                    operador = comando;
                    nuevoNumero = true;
                }
            } else {
                if (nuevoNumero) {
                    Pantalla.setText(comando);
                    nuevoNumero = false;
                } else {
                    Pantalla.setText(Pantalla.getText() + comando);
                }
            }
        }

        private void calcularResultado() {
            if (!Pantalla.getText().isEmpty() && !operador.isEmpty()) {
                double segundoNumero = Double.parseDouble(Pantalla.getText());
                double resultado = 0;

                if (operador.equals("+")) {
                    resultado = primerNumero + segundoNumero;
                } else if (operador.equals("-")) {
                    resultado = primerNumero - segundoNumero;
                } else if (operador.equals("×")) {
                    resultado = primerNumero * segundoNumero;
                } else if (operador.equals("÷")) {
                    if (segundoNumero != 0) {
                        resultado = primerNumero / segundoNumero;
                    } else {
                        resultado = 0;
                    }
                }

                Pantalla.setText(String.valueOf(resultado));
                primerNumero = resultado;
            }
        }
    }
}
