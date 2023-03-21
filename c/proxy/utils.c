//
// Created by void on 3/21/23.
//

#include "utils.h"
#include "lib_tcp.h"

#include <errno.h>

#include <stdlib.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <string.h>
#include <stdio.h>

int log_func(int func_result, char* log_msg) {
    printf("%s: ", log_msg);

    if (func_result < 0) { // == -1
        printf("FAILED (%d)\n", func_result);
        printf("=== Error: %s ===", strerror(errno));
        return -1;
    } else {
        printf("OK (%d)\n", func_result);
        return func_result;
    }
}

void write_to_file(char* path, char* string) {
    FILE* file = fopen(path, "w");
    fprintf(file, "%s", string);

    printf("WRITING TO FILE: %s, LEN:%lu\n", path, strlen(string));
    fclose(file);
}

int wait_interrupt(char* msg_print) {
    printf("%s", msg_print);
    char *q1 = malloc(sizeof(char) * 10);

    scanf("%s", q1);
    if (q1[0] == 'y') {
        return 1;
    } else {
        return 0;
    }
}


int get_server_port(int argn, char** argv) {
    if (argn > 1) {
        return (int) strtol(argv[1], NULL, 10);
    } else {
        printf("setting SERVER_PORT to default: %d\n", DEFAULT_SERVER_PORT);
        return DEFAULT_SERVER_PORT;
    }
}

void setup_server_addr(struct sockaddr_in* server_addr, int SERVER_PORT) {
    memset(server_addr, 0, sizeof(*server_addr));
    server_addr->sin_family = AF_INET;
    server_addr->sin_addr.s_addr = INADDR_ANY; // inet_addr(SERVER_IP_ADDR);
    server_addr->sin_port = htons(SERVER_PORT);
}


void print_sockfd_info(int sockfd) {
    struct sockaddr_in conn_addr;
    socklen_t addr_len = sizeof(conn_addr);
    getsockname(sockfd, (struct sockaddr *)&conn_addr, &addr_len);
    printf("\n===== %d =====\n", sockfd);
    printf("Socket address: %s\n", inet_ntoa(conn_addr.sin_addr));
    printf("Socket port: %d\n", ntohs(conn_addr.sin_port));
    printf("=====   =====\n");
}
