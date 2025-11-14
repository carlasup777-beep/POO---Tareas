# POO---Tareas
Programación orientada a objetos tareas

# Sistema de Gestión de Vehículos - POO en Python

## Descripción del Proyecto

Este programa simula un sistema de vehículos usando Programación Orientada a Objetos. Incluye una clase Motor y una superclase Vehiculo de la cual heredan Automovil y Motocicleta. Cada vehículo tiene su propio motor y métodos específicos.

## Conceptos de POO Aplicados

**Encapsulamiento**: Los atributos son privados (con `_`) y se accede a ellos mediante `@property` y `@setter`. Esto permite validar los datos antes de asignarlos.

**Herencia**: Vehiculo es la clase padre. Automovil y Motocicleta heredan sus atributos y métodos, añadiendo características propias de cada tipo.

**Composición**: Tanto Automovil como Motocicleta tienen un objeto Motor. Esta relación "tiene-un" permite que el motor sea independiente pero funcione junto al vehículo.

**Polimorfismo**: El método `__str__()` está implementado en todas las clases. Cada una lo sobrescribe para mostrar su información específica usando `super()`.

## Estructura del Código

El programa tiene 4 clases:

- **Motor**: Clase independiente con tipo y potencia. Tiene métodos para encender y apagar el motor.

- **Vehiculo**: Clase base con marca, modelo, año y un motor. Incluye métodos básicos como encender y apagar.

- **Automovil**: Hereda de Vehiculo y añade numero_puertas. Tiene métodos para abrir el maletero y tocar el claxon.

- **Motocicleta**: Hereda de Vehiculo y añade cilindraje. Puede hacer caballitos y tiene arranque con patada.

## Cómo Ejecutar

```bash
python sistema_vehiculos.py
```

El programa necesita Python 3.7 o superior.

## Funcionamiento

El programa principal crea 2 automóviles y 2 motocicletas, cada uno con su motor. Luego ejecuta varios métodos de cada vehículo para demostrar que todo funciona correctamente.

Se crean 4 motores diferentes (V8, eléctrico, monocilíndrico y bicilíndrico) y se asignan a los vehículos correspondientes. Después se prueba encenderlos, usar sus funciones específicas y apagarlos.

Al final muestra un resumen con la información de todos los vehículos usando el método `__str__()`.

## Validaciones Implementadas

- La potencia del motor debe ser mayor a 0
- El año del vehículo debe ser mayor a 1900
- El número de puertas solo puede ser 2, 3, 4 o 5
- El cilindraje debe ser positivo
- No se puede hacer caballito si la moto está apagada

## Ejemplo de Salida

```
CREACIÓN DE AUTOMÓVILES
Chevrolet Camaro (2024) - Auto de 2 puertas
   Motor V8 Gasolina de 450 HP

Tesla Model 3 (2023) - Auto de 4 puertas
   Motor Eléctrico de 300 HP
```
