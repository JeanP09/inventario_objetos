CREATE DATABASE fabrica;
USE fabrica;

-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 08-05-2024 a las 05:55:16
-- Versión del servidor: 10.4.25-MariaDB
-- Versión de PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `fabrica`



-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `devoluciones`
--

CREATE TABLE `devoluciones` (
  `IdDevoluciones` int(11) NOT NULL,
  `IdUsuario` int(11) DEFAULT NULL,
  `IdPrestamo` int(11) DEFAULT NULL,
  `IdProducto` int(11) DEFAULT NULL,
  `FechaHoraDevolucion` datetime DEFAULT NULL,
  `EstadoDevolucion` enum('BUENO','MAL ESTADO') DEFAULT NULL,
  `Observaciones` varchar(225) DEFAULT NULL,
  `ModoTiempoLugar` varchar(225) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `prestamos`
--

CREATE TABLE `prestamos` (
  `IdPrestamo` int(11) NOT NULL,
  `IdUsuario` int(11) DEFAULT NULL,
  `IdProducto` int(11) DEFAULT NULL,
  `FechaHoraPrestamo` datetime DEFAULT NULL,
  `CantidadPrestamo` int(11) DEFAULT NULL,
  `ObservacionesPrestamo` varchar(225) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productosgenerales`
--

CREATE TABLE `productosgenerales` (
  `IdProducto` int(11) NOT NULL,
  `NombreProducto` varchar(225) DEFAULT NULL,
  `DescripcionProducto` varchar(225) DEFAULT NULL,
  `TipoProducto` enum('Devolutivos','Consumibles/Formación') DEFAULT NULL,
  `CantidadProducto` int(11) DEFAULT NULL,
  `ObservacionesProducto` varchar(225) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--
CREATE TABLE `usuarios` (
  `IdUsuario` int NOT NULL AUTO_INCREMENT,
  `NombreUsuario` varchar(255) DEFAULT NULL,
  `ApellidoUsuario` varchar(255) DEFAULT NULL,
  `TipoIdentificacion` enum('CC','TI') DEFAULT NULL,
  `NumeroIdentificacion` int(11) DEFAULT NULL,
  `CorreoUsuario` varchar(255) DEFAULT NULL,
  `CelularUsuario` int(11) DEFAULT NULL,
  `ContrasenaUsuario` varchar(50),
  PRIMARY KEY (`IdUsuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
INSERT INTO usuarios (NombreUsuario, ApellidoUsuario, TipoIdentificacion, NumeroIdentificacion, CorreoUsuario, CelularUsuario, ContrasenaUsuario)
VALUES
    ('Santiago', 'Urrea', 'CC', 1031648741, 'santi@gmail.com',  3246016033, 'santi777');
	select*from usuarios;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `devoluciones`
--
ALTER TABLE `devoluciones`
  ADD PRIMARY KEY (`IdDevoluciones`),
  ADD KEY `IdUsuario` (`IdUsuario`),
  ADD KEY `IdPrestamo` (`IdPrestamo`),
  ADD KEY `IdProducto` (`IdProducto`);

--
-- Indices de la tabla `prestamos`
--
ALTER TABLE `prestamos`
  ADD PRIMARY KEY (`IdPrestamo`),
  ADD KEY `IdUsuario` (`IdUsuario`),
  ADD KEY `IdProducto` (`IdProducto`);

--
-- Indices de la tabla `productosgenerales`
--
ALTER TABLE `productosgenerales`
  ADD PRIMARY KEY (`IdProducto`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`IdUsuario`);
ALTER TABLE `usuarios`
  ADD `ContrasenaUsuario` varchar(50) 
--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `devoluciones`
--
ALTER TABLE `devoluciones`
  MODIFY `IdDevoluciones` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `prestamos`
--
ALTER TABLE `prestamos`
  MODIFY `IdPrestamo` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `productosgenerales`
--
ALTER TABLE `productosgenerales`
  MODIFY `IdProducto` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `IdUsuario` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `devoluciones`
--
ALTER TABLE `devoluciones`
  ADD CONSTRAINT `devoluciones_ibfk_1` FOREIGN KEY (`IdUsuario`) REFERENCES `usuarios` (`IdUsuario`),
  ADD CONSTRAINT `devoluciones_ibfk_2` FOREIGN KEY (`IdPrestamo`) REFERENCES `prestamos` (`IdPrestamo`),
  ADD CONSTRAINT `devoluciones_ibfk_3` FOREIGN KEY (`IdProducto`) REFERENCES `productosgenerales` (`IdProducto`);

--
-- Filtros para la tabla `prestamos`
--
ALTER TABLE `prestamos`
  ADD CONSTRAINT `prestamos_ibfk_1` FOREIGN KEY (`IdUsuario`) REFERENCES `usuarios` (`IdUsuario`),
  ADD CONSTRAINT `prestamos_ibfk_2` FOREIGN KEY (`IdProducto`) REFERENCES `productosgenerales` (`IdProducto`);
COMMIT;



/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
